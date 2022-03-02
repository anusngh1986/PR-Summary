# PR-Summary
A python utility to retrieve a summary of all opened, closed, and in progress pull requests for a given Github repository within some time frame, with optional email output.

## Prerequisite
1. Python with version 3.8 or above should be installed in machine.
2. Install python request module used for making API calls using below commad.

**"pip install requests"**

## Script Usage
Execution of script will start with main.py.

**python main.py --org PyGithub --repo PyGithub --email anusngh1986@gmail.com**

In order to have the output sent as an email, you must create a `credentials.json` file in the same directory as `main.py`.  This file should look something like this:
``` json
{
    "smtp_host": "smtp.gmail.com",
    "smtp_port": 465,
    "username": "SoAndSo@gmail.com",
    "password": "SoAndSoSPasSWord"
}
```

If the intended solution is to use gmail, you'll have to [make an app specific password](https://support.google.com/accounts/answer/185833?hl=en) and use that password in the credential.json file.  In addition, the `--email` parameter must be provided to the script.

## Argument Reference
- `--org`, a required, case-sensitive string argument that indicates which public github organization the repository lives in.
- `--repo`, a required, case-sensitive string argument that indicates which public github repository to look at.
- `--timeframe`, The number of days to look back in time. (the default is 7)
- `--email`, The email you want to send the results of the script run to.  (If not provided, output will be to console.)

## Example Script Output
When I ran the script using below command on Feb 3rd, 2022.This was the console output I received.

**python main.py --org PyGithub --repo PyGithub --timeframe 20**
```
Script Output:
FROM: no-reply@gmail.com.com
TO: notprovided@nodomain.com
SUBJECT: Pull Request report for PyGithub/PyGithub for the 20 days preceding 2022-03-02
BODY:
Greetings!

**Pull Requests Opened:**
PR #2190 - Get all secrets from org by gerardsegarra - Link: https://github.com/PyGithub/PyGithub/pull/2190
PR #2189 - Initial commit by POCO by manju-prasad - Link: https://github.com/PyGithub/PyGithub/pull/2189
PR #2183 - feat: no update git refs method  by mittal-umang - Link: https://github.com/PyGithub/PyGithub/pull/2183
PR #2172 - Fix get events not returning user events by ncareau - Link: https://github.com/PyGithub/PyGithub/pull/2172
**Pull Requests In Progress:**
PR #2090 - Create repo from template by simkimsia - Link: https://github.com/PyGithub/PyGithub/pull/2090
**Pull Requests Closed:**
PR #2188 - Initial commit by POCO by manju-prasad - Link: https://github.com/PyGithub/PyGithub/pull/2188
PR #2187 - Initial commit by POCO by manju-prasad - Link: https://github.com/PyGithub/PyGithub/pull/2187
PR #2186 - Initial commit by POCO by manju-prasad - Link: https://github.com/PyGithub/PyGithub/pull/2186
PR #2185 - Initial commit by POCO Orig by manju-prasad - Link: https://github.com/PyGithub/PyGithub/pull/2185
PR #2184 - Use 'requests' instead of 'httplib' by manju-prasad - Link: https://github.com/PyGithub/PyGithub/pull/2184
```
