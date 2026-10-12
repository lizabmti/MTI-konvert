class Convert:
    @staticmethod
    def perevesti(summa,rate_from,rate_to):
        if rate_from<=0:
            return 0
        return summa/rate_from*rate_to
