import main
import multi_training
pcs = multi_training.loadPieces("music")

import model
m = model.Model([300,300],[100,50], dropout=0.5)
m.learned_config = pickle.read(open('output/params4000.p', 'rb'))
main.gen_adaptive(m,pcs,10,name="composition")
