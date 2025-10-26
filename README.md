# 🎓 graduation_project_URALSIB

*Дипломный проект по автоматизации страницы УралСиб Банка*

## О проекте

Этот проект является дипломной работой по курсу QA.GURU и представляет собой фреймворк для автоматизации тестирования веб-приложения "UralSib" (https://uralsib.ru). В реализации использованы инструменты и библиотеки:

<p  align="center">
  
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" height="100" width="100"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg" height="100" width="100"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original.svg" height="100" width="100"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original.svg" height="100" width="100"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/selenium/selenium-original.svg" height="100" width="100"/>
  <code><img width="13%" title="Selene" src="data/logo/selene.png" alt="selene"/></code>
  <code><img width="13%" title="Allure Report" src="data/logo/allure_report.png" alt="allure"></code>
  <code><img width="13%" title="Allure Report" src="data/logo/allure_testops.png" alt="alluretest"></code>
  <code><img width="13%" title="Allure Report" src="data/logo/selenoid.png" alt="selenoid"></code>
  <code><img width="13%" title="Allure Report" src="data/logo/tg.png" alt="tg"></code>
</p>

## <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" height="20" width="20"> Запуск тестов локально

1) Клонировать репозиторий: git clone https://github.com/MozzhukhinRA/graduation_project
2) Активировать окружение и установить зависимости: poetry shell, poetry install
3) Запуск тестов: pytest .
4) генерацией отчетов Allure: allure serve allure-results

##   <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg" height="20" width="20"/> Создание сборки на удаленном сервере - Jenkins

1) Авторизоваться в Jenkins
2) Перейти в джобу https://jenkins.autotests.cloud/job/MozzhukhinRA_graduation_project_ui
3) Для запуска тестов в Jenkins нажать "Build Now"

<p><img title="jenkins_build" src="data/logo/jen1.png"></p>

## <img width="4%" title="allure" src="data/logo/allure_report.png"> Визуализация результатов (Allure Reports и Allure TestOps)

Для просмотра результатов тестового прогона в Allure клик на соответствующую ему иконку

<p><img title="allure" src="data/logo/img.png"></p>
<p><img title="allure" src="data/logo/img_allure.png"></p>
<p><img title="allure" src="data/logo/img_allure_2.png"></p>



Для просмотра результатов тестового прогона в Allure TestOps кликнув на соответствующую ему иконку в джобе Jenkins

<p><img title="allure_testops" src="data/logo/job_testops.png"></p>
<p><img title="allure_testops" src="data/logo/img_testops.png"></p>

Так же проверить аттачменты - логи, скриншот, видео. Можно, перейдя в раздел "Запуски", завершить Job и провалиться в него

<p><img title="allure_testops" src="data/logo/job.png"></p>
<p><img title="allure_testops" src="data/logo/attach.png"></p>



## <img width="4%" title="tg" src="data/logo/tg.png"> Интеграция с Telegram в Jenkins для автоматической отправки результатов тестового прогона через бота

<p><img title="telegram" src="data/logo/report_tg.png"></p>
