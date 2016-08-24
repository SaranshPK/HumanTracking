tempBlobs.append(Blob(currentSize, (r, g, b), midpoint, uuid.uuid1()))
    for blob in blobs:
        closestBlob = None
        minDist = None
        for ablob in tempBlobs:
            if closestBlob == None:
                closestBlob = ablob
                minDist = math.sqrt(math.pow(closestBlob.midpoint[0], 2) + math.pow(closestBlob.midpoint[1], 2))
            dist = math.sqrt(math.pow(ablob.midpoint[0],2)+math.pow(ablob.midpoint[1], 2))
            if(dist<minDist):
                closestBlob = ablob
                minDist = dist
        if(minDist<10):
            blob.blobSize = closestBlob.blobSize
            blob.midpoint = closestBlob.midpoint
            blob.color = closestBlob.color
            tempBlobs.remove(closestBlob)
    for blob in tempBlobs:
        blobs.append(tempBlobs)