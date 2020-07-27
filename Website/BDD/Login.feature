Feature:Login

  Scenario Outline: Using right account to login QQMail
    Given I load QQMail website
    When I input right "<username>" and "<password>"
    Then I can enter this QQMail
    Examples:
      | username  | password |
      | 454216847 | gy329329 |


  Scenario Outline: Using wrong account to login QQMail
    Given I load QQMail website
    When I input wrong "<username>" and "<password>"
    Then I can not enter this QQMail
    Examples:
      | username  | password |
      | 454216847 | 123456   |