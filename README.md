ci / cd pipeline

- run the flake8 linter (report warnings?) and radon / xenon to check complexity (or just use flake8)
- use a kanban tool like trello for sprint planning
- get test coverage and report etc.
- run the test suite (seperate unit and integration, only run integration on nightly)
- create ci, nightly and release definitions, with different build jobs
- create branch strategy (dev and tagged release branches)
- the release deifinition should deploy to the actual server
- the integration definition should test against a test server
- the ci definition shouldn't interact with azure at all, mock the shite out of everything
- run nightly nightly, run ci on pull requests onto any pushed branch that isn't release and prs onto dev
- create tags to kick off deployment build
- use github secrets for connection strings and the like
- use tdd
- the release should be a zip file or similar to publish with internal configuration scripts /file + short user guide 
- plans for improvement 
	- set up auto reporting of failures to dev mailing list
	- manual blue green testing before release
	- use senior manager gpg signed tag to initiate release
	- use release candidate branches etc.

Project Board:
https://trello.com/b/arxBSkXl/project
