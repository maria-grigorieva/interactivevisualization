class CalculationBase:

    __is_cluster_analysis = False

    def get_is_cluster_analysis(self):
        return self.__is_cluster_analysis

    is_cluster_analysis = property(get_is_cluster_analysis)

    def perform(self, data, parameters):
        return None

