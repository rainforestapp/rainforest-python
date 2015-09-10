from ..apibits import ApiClient

class DefaultClient(ApiClient):

    def __init__(self, api_key):
        self.refresh_from(api_key)

    def refresh_from(self, api_key):
        headers = {
            "Accept" : "application/json",
            "Content-Type" : "application/json",
            "CLIENT_TOKEN" : api_key,
        }
        params = {
        }
        super(DefaultClient, self).refresh_from(headers, params)
        return self

    def client_stats(self):
        from ..endpoints import ClientStatsEndpoint
        return ClientStatsEndpoint(self)

    def environments(self):
        from ..endpoints import EnvironmentsEndpoint
        return EnvironmentsEndpoint(self)

    def generators(self):
        from ..endpoints import GeneratorsEndpoint
        return GeneratorsEndpoint(self)

    def integrations(self):
        from ..endpoints import IntegrationsEndpoint
        return IntegrationsEndpoint(self)

    def runs(self):
        from ..endpoints import RunsEndpoint
        return RunsEndpoint(self)

    def schedules(self):
        from ..endpoints import SchedulesEndpoint
        return SchedulesEndpoint(self)

    def site_environments(self):
        from ..endpoints import SiteEnvironmentsEndpoint
        return SiteEnvironmentsEndpoint(self)

    def sites(self):
        from ..endpoints import SitesEndpoint
        return SitesEndpoint(self)

    def tests(self):
        from ..endpoints import TestsEndpoint
        return TestsEndpoint(self)

    def users(self):
        from ..endpoints import UsersEndpoint
        return UsersEndpoint(self)
