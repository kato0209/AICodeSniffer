if old is None: return new <extra_id_0> isinstance(old, list): old = old[:] new = new[:] else: old = old.split(',') new = new.split(',') if len(old)!= len(new): <extra_id_1> ValueError('Cannot <extra_id_2> %s and %s' % (old, new)) for i in range(len(old)): if old[i]!= new[i]: raise ValueError('Cannot merge %s and %s' % (old[i], new[i])) return new <extra_id_3> _merge_dict(self,