
        jmodel = callBigDlFunc(bigdl_type, "loadCaffe", model, defPath, modelPath, match_all)
        return Layer.of(jmodel)