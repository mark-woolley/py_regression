import statsmodels.formula.api as smf

class RunRegression(object):

    def __init__(self, df, formula):
        self._df = df
        self._formula = formula

    @property
    def results(self):
        return self._run_regression()

    def _run_regression(self):

        model = smf.ols(formula=self._formula, data=self._df)
        fit = model.fit()
        print(fit.summary())

        return fit
