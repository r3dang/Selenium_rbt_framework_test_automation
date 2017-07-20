*** Settings ***
Library     Selenium2Library

Suite Setup  Go to homepage
Suite Teardown  Close all browsers


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

