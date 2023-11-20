param location string
param jobName string
param environmentId string
param env array
param image string
param cpu string
param memory string
param workloadProfileName string
param cronExpression string
param replicaCompletionCount int
param parallelism int
param replicaRetryLimit int
param replicaTimeout int
param triggerType string

resource job 'Microsoft.App/jobs@2023-05-02-preview' = {
  name: jobName
  location: location
  properties: {
    configuration: {
      scheduleTriggerConfig: {
        cronExpression: cronExpression
        replicaCompletionCount: replicaCompletionCount
        parallelism: parallelism
      }
      replicaRetryLimit: replicaRetryLimit
      replicaTimeout: replicaTimeout
      triggerType: triggerType
    }
    environmentId: environmentId
    template: {
      containers: [
        {
          name: 'ticketkantoor-event-scraper'
          env: env
          image: image
          resources: {
            cpu: json(cpu)
            memory: memory
          }      
        }
      ]
    }
    workloadProfileName: workloadProfileName
  }
}

output id string = job.id
output name string = job.name
