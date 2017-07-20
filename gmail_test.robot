*** Settings ***
Library     Selenium2Library

Suite Setup  Go to homepage
Suite Teardown  Close all browsers

# Having trouble with importing selenium2library
# I have already installed it with pip
# when I run installtion script on pip3, there is a syntax error
# so there is nothing that I can do.
# in pyCharm, it is not recognizing the Selenium2Library.

*** Variables ***
${HOMEPAGE}     https://www.google.com
${BROWSER}      chrome

*** Test Cases ***
Google DevOps and find eficode

*** Keywords ***
Google and check results
    [Arguments]     ${searchkey}    ${result}

Go to homepage
    Open Browser    ${HOMEPAGE}     ${BROWSER}

