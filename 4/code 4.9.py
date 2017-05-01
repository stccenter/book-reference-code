>>> def drawMap():
	for i in range(len(layers)):
		if (layers[i].layerType == 'Image'):
		    continue
		layers[i].drawLayer()
        
