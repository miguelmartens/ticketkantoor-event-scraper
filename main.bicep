param containerAppName string
param imageName string
param cpuCores string = '0.5'
param memory string = '1.0Gi'
param cronSchedule string = '0 */1 * * *' // Every hour, adjust as needed
param timeoutSeconds = 600

// Include the container app job module
module containerAppJob './modules/container-app-job.bicep' = {
  name: '${containerAppName}-job-module'
  params: {
    containerAppName: containerAppName
    imageName: imageName
    cpuCores: cpuCores
    memory: memory
    cronSchedule: cronSchedule
    timeoutSeconds: timeoutSeconds
  }
}

output jobResourceId string = containerAppJob.outputs.jobResourceId
