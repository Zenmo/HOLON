
def validateInputs(experiment):
    print("ECHO: starting input data validation...")
    print(experiment.rawData)

    #print(experiment.rawData.keys())
    
    definedGridNodes = experiment.rawData["config_gridNodes"]
    definedActors = experiment.rawData["config_actors"]
    definedGridConnections = experiment.rawData["config_gridConnections"]
    definedEnergyAssets = experiment.rawData["config_energyAssets"]

    # check for non-existent actors:
    
    actorIDList = definedActors["id"]
    gridConnectionOwners = definedGridConnections["owner_actor"]
    
    #owner = gridConnectionOwners[2]
    #print(owner)    
#    print(test2)
    #print(definedGridConnections['owner_actor'])
    #print(definedActors['id'])

    def checkAssingment(listOfReferencedElements, listOfDefinedElements):
        # check if all of the referenced elements exist in the list of all defined elements
        listOfErrorValues = []
        for x in listOfReferencedElements:
            count = sum(map(lambda y : y == x , listOfDefinedElements))    
            if count == 0:
                listOfErrorValues.append(x)
                
        if len(listOfErrorValues) > 0:
            return listOfErrorValues
        else:
            return None
    
    print("check 1: assigning gridconnections to non-existent actors...")
    errorActor = checkAssingment(definedGridConnections['owner_actor'], definedActors['id'])
    if errorActor != None:
        print('>>> Configuration Error #1: referenced owner_actor: \'', errorActor,'\' is not defined!')
        #raise ValueError('Configuration Error #1: gridConnection(s) assigned to non-existing owner_actor!')

    print("check 2: assigning connection_owners to non-existent parent actors...")
    errorActor = checkAssingment(definedActors['parent_actor'], definedActors['id'])
    if errorActor != None:
        print('>>> Configuration Error #2: referenced parent-actor \'', errorActor, '\' is not defined! ')
        #raise ValueError('Configuration Error #2: actor(s) assigned to non-existing parent-actor!')
        
    print("check 3: assigning energy assets to non-existent gridConnections...")
    errorActor = checkAssingment(definedEnergyAssets["parent"], definedGridConnections["id"])
    if errorActor != None:
        print('>>> Configuration Error #3: referenced gridConnection \'', errorActor, '\' is not defined! ')
        #raise ValueError('Configuration Error #3: energyAsset(s) assigned to non-existing gridConnection!')
     
    print("check 4: assigning gridConnections to non-existing gridNodes")
    errorActor = checkAssingment(definedGridConnections["parent_electric"], definedGridNodes["id"])
    if errorActor != None:
        print('>>> Configuration Error #4: referenced gridNode \'', errorActor, '\' is not defined!')
        #raise ValueError('Configuration Error #4: gridConnection(s) assigned to non-existing gridNode!')
    
    print("check 5: assinging non HSMS-gridNodes to non-existent gridNodes")
    errorActor = checkAssingment(definedGridNodes[definedGridNodes['type2']!="HSMS"]["parent"], definedGridNodes["id"])
    if errorActor != None:
        print('>>> Configuration Error #5: referenced gridNode \'', errorActor, '\' is not defined!')
        #raise ValueError('Configuration Error #5: gridNode(s) assigned to non-existing gridNode!')
          
    print("check 6: assinging gridNodes to non-existent owner-actors")
    errorActor = checkAssingment(definedGridNodes["owner"], definedActors["id"])
    if errorActor != None:
        print('>>> Configuration Error #6: referenced owner-actor \'', errorActor, '\' is not defined!')
        #raise ValueError('Configuration Error #6: gridNode(s) assigned to non-existing owner-actor!')
  
    #print("actors::: ",definedActors)
    #print("gridConnections::: ",definedGridConnections)
    print("ECHO: input data validation finished!")
    return experiment
