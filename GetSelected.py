from findCurrentSystem import returnAll, returnSoftware

def Setup_data(SelectedAsset):      #gets all asset information, formats it in a 2d array and finds the asset being searched for
    getAllresult = returnAll()
    datafetch = [list(item) for item in getAllresult]
    dataset = []
    for item in datafetch:
        innerlist = []
        for field in item:
            innerlist.append(field)
        dataset.append(innerlist)
    AffetedRow = dataset[SelectedAsset]
    data = AffetedRow
    return data

def SoftwareData(SelectedAsset):
    getAllresult = returnSoftware()
    datafetch = [list(item) for item in getAllresult]
    dataset = []
    for item in datafetch:
        innerlist = []
        for field in item:
            innerlist.append(field)
        dataset.append(innerlist)
    AffetedRow = dataset[SelectedAsset]
    data = AffetedRow
    return data

def returnItem(SelectedAsset):
    data = Setup_data(SelectedAsset)
    return data

def returnSelectedSoftware(SelectedAsset):
    data = SoftwareData(SelectedAsset)
    return data
