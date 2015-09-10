
API_KEY = None

API_BASE = "https://app.rainforestqa.com/api/1"

from .clients import DefaultClient
from .resources import (ClientStats, Environment, Generator, Integration, Run, Schedule, SiteEnvironment, Site, Test, User, )
from .endpoints import (ClientStatsEndpoint, EnvironmentRunsEndpoint, EnvironmentsEndpoint, GeneratorsEndpoint, GeneratorRowsEndpoint, IntegrationsEndpoint, RunTestsEndpoint, RunsEndpoint, SchedulesEndpoint, SiteEnvironmentsEndpoint, SitesEndpoint, TestsEndpoint, UsersEndpoint, )

def default_client():
	return DefaultClient(API_KEY)