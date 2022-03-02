import requests
from .date_parsing import reParseDate

from requests.api import request

def isPRTooOld(PRobj, cutoffTime): #Check for update date of PR
    updateTime = PRobj['updated_at']
    PRTime = reParseDate(updateTime)
    return cutoffTime > PRTime
    
def getCutoffTime(currentDate, timeDelta):
    return (currentDate - timeDelta)

def get_PRs(org,repo,pr_state = 'all',page_number = 1,req_module = requests):
    return req_module.get(f'https://api.github.com/repos/{org}/{repo}/pulls',{'state':pr_state,'sort':'updated', 'direction':'desc','page':page_number})

def get_Recent_PRs(currentDate, timeDelta, org, repo, pr_state = 'all', req_module = requests):
    jsonCollection = []
    page_number = 0
    cutoffDate = getCutoffTime(currentDate, timeDelta)
    foundCutoff = False #Variable to find if we are not going beyond specified days(i.e 7 days).

    while (not foundCutoff):
        page_number = page_number + 1
        requestResult = get_PRs(org,repo,pr_state,page_number,req_module).json()
        if (requestResult == []): # We've exceeded the number of pages
            foundCutoff = True
            break

        index = 0 #Pointer for moving inside list indices
        while (index < len(requestResult) and not foundCutoff):
            foundCutoff = isPRTooOld(requestResult[index], cutoffDate)
            if (not foundCutoff):
                index = index + 1
        
        if (not foundCutoff or index > len(requestResult)): #So we went all the way through the first page and we haven't found the end of the PRs in the time span we want.
            jsonCollection = jsonCollection + requestResult
        elif (foundCutoff): #we found the PR in the list that is too old to care about, so append to that point and truncate the rest.
            jsonCollection = jsonCollection + (requestResult[0:index])

    return jsonCollection
    
def SortPRs(jsonCollection, currentDate, timeDelta):
    openedPRs = []
    closedPRs = []
    inProgressPRs = []
    cutoffTime = getCutoffTime(currentDate, timeDelta)

    for pr in jsonCollection:
        if (pr['state'] == 'open'): #If the state is open, but it was made before our cutoff search time it's in progress
            if cutoffTime > reParseDate(pr['created_at']):
                inProgressPRs = inProgressPRs + [pr]
            else:
                openedPRs = openedPRs + [pr]
        elif (pr['state'] == 'closed' and cutoffTime < reParseDate(pr['closed_at'])):
            closedPRs = closedPRs + [pr]

    return {
        'open': openedPRs,
        'closed': closedPRs,
        'in-progress': inProgressPRs
    }
