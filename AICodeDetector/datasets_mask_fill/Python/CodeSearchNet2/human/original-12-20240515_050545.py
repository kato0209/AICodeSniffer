

        jresults = callBigDlFunc(self.bigdl_type,
                             "predictLocal",
                               self.value,
                               self._to_jtensors(X),
                          