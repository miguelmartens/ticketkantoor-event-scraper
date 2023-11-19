param containerAppName string
param imageName string
param cpuCores string
param memory string
param cronSchedule string
param timeoutSeconds int

resource containerApp 'Microsoft.Web/containerApps@2021-03-01' = {
  name: containerAppName
  location: resourceGroup().location
  properties: {
    configuration: {
      activeRevisionsMode: 'Multiple'
      ingress: {
        external: true
        targetPort: 80
      }
    }
    template: {
      containers: [
        {
          name: containerAppName
          image: imageName
          resources: {
            cpu: cpuCores
            memory: memory
          }
        }
      ]
      scale: {
        minReplicas: 0
        maxReplicas: 1
        rules: [
          {
            name: 'httpscalingrule'
            custom: {
              type: 'http'
              metadata: {
                concurrentRequests: '50'
              }
            }
          }
        ]
      }
      dapr: {
        enabled: false
      }
      revisionSuffix: '-rev'
    }
  }
  kind: 'containerApp'
}

resource containerAppJob 'Microsoft.Web/containerApps/jobs@2021-03-01' = {
  parent: containerApp
  name: 'myJob'
  properties: {
    schedule: {
      cron: cronSchedule
    }
    task: {
      container: {
        name: containerAppName
        image: imageName
        resources: {
          cpu: cpuCores
          memory: memory
        }
      }
      timeoutSeconds: timeoutSeconds
    }
  }
}

