
param location string = resourceGroup().location

param sku string = 'PerNode'
param logAnalyticsWorkspaceName string
param retentionInDays int = 30

param managedEnvironmentName string
param workloadProfileName string = 'Consumption'
param workloadProfileType string = 'Consumption'

param jobName string
param cpu string = '0.25'
param cronExpression string
param image string
param memory string = '0.5Gi'
param parallelism int = 1
param replicaCompletionCount int = 1
param replicaRetryLimit int = 1
param replicaTimeout int = 60
param triggerType string = 'Schedule'

param ticketkantoorEmail string
@secure()
param ticketkantoorPassword string
param userObjectId string
param recipientEmail string
param graphApiClientId string
@secure()
param graphApiClientSecret string
param graphApiTenantId string
param useEmailUtils string = 'true'
param eventName string

module logAnalyticsWorkspace './modules/log-analytics-workspace.bicep' = {
  name: 'logAnalyticsWorkspace'
  scope: resourceGroup()
  params: {
    location: location
    sku: sku
    logAnalyticsWorkspaceName: logAnalyticsWorkspaceName
    retentionInDays: retentionInDays
  }
}

module managedEnvironment './modules/managed-environment.bicep' = {
  name: 'managedEnvironment'
  scope: resourceGroup()
  params: {
    location: location
    customerId: logAnalyticsWorkspace.outputs.customerId
    managedEnvironmentName: managedEnvironmentName
    workloadProfileName: workloadProfileName
    workloadProfileType: workloadProfileType
  }
}

module job './modules/container-apps-job.bicep' = {
  name: 'job'
  params: {
    location: location
    cpu: cpu
    cronExpression: cronExpression
    env: [
      {
        name: 'TICKETKANTOOR_EMAIL'
        value: ticketkantoorEmail
      }
      {
        name: 'TICKETKANTOOR_PASSWORD'
        value: ticketkantoorPassword
      }
      {
        name: 'USER_OBJECT_ID'
        value: userObjectId
      }
      {
        name: 'RECIPIENT_EMAIL'
        value: recipientEmail
      }
      {
        name: 'GRAPH_API_CLIENT_ID'
        value: graphApiClientId
      }
      {
        name: 'GRAPH_API_CLIENT_SECRET'
        value: graphApiClientSecret
      }
      {
        name: 'GRAPH_API_TENANT_ID'
        value: graphApiTenantId
      }
      {
        name: 'USE_EMAIL_UTILS'
        value: useEmailUtils
      }
      {
        name: 'EVENT_NAME'
        value: eventName
      }
    ]
    environmentId: managedEnvironment.outputs.id
    image: image
    jobName: jobName
    memory: memory
    parallelism: parallelism
    replicaCompletionCount: replicaCompletionCount
    replicaRetryLimit: replicaRetryLimit
    replicaTimeout: replicaTimeout
    triggerType: triggerType
    workloadProfileName: workloadProfileName
  }
}
