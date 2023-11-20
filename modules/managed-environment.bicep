param location string
param managedEnvironmentName string
param customerId string
param workloadProfileType string
param workloadProfileName string
param logAnalyticsWorkspaceName string

resource logAnalyticsWorkspace 'Microsoft.OperationalInsights/workspaces@2022-10-01' existing = {
  name: logAnalyticsWorkspaceName
}
resource managedEnvironment 'Microsoft.App/managedEnvironments@2023-05-02-preview' = {
  name: managedEnvironmentName
  location: location
  properties: {
    appLogsConfiguration: {
      destination: 'log-analytics'
      logAnalyticsConfiguration: {
        customerId: customerId
        sharedKey: logAnalyticsWorkspace.listKeys().primarySharedKey
      }
    }
    zoneRedundant: false
    workloadProfiles: [
      {
        workloadProfileType: workloadProfileType
        name: workloadProfileName
      }
    ]
  }
}

output id string = managedEnvironment.id
output name string = managedEnvironment.name
output appLogsConfiguration object = managedEnvironment.properties.appLogsConfiguration
