PythonProject1 — проект под ТЗ «подготовка к пересдаче» с полным CI/CD

Ссылки
- Репозиторий: https://github.com/mo1kx/pythonproject1
- Docker Hub: https://hub.docker.com/r/mo1kx/pythonproject1

Что установлено и где зарегистрирован
- Git, Docker Desktop, PyCharm
- Аккаунты: GitHub, Docker Hub, Telegram (бот)

Секреты в GitHub (Settings → Secrets and variables → Actions)
- DOCKERHUB_USERNAME — логин Docker Hub
- DOCKERHUB_TOKEN — токен Docker Hub (Read/Write)
- TELEGRAM_BOT_TOKEN — токен бота от @BotFather
- TELEGRAM_CHAT_ID — id чата/канала для уведомлений

Как работать (ветки и PR)
- Новые задачи: ветки `feature/...`
- Срочные исправления: `hotfix/...` (слово hotfix укажи в заголовке PR)
- Создай PR → запускаются проверки (pytest, безопасность). При успехе PR получает лейблы `test-passed`, `sec-passed` и авто‑комментарий с итогом.
- Merge в `main` запускает релиз: bump версии, CHANGELOG, сборка и публикация образа в DockerHub (`<user>/pythonproject1:<version>` и `latest`), обновление описания DockerHub, Telegram‑уведомление, GitHub Release, деплой на self‑hosted (если раннер подключён).

Порядок проверки работы (из ТЗ)
1) Ссылка на репозиторий — см. выше.
2) .github/workflows — настроены `pr.yml` и `release.yml`.
3) Pull Request — авто‑лейблы (`feature`/`hotfix`, `test-passed`, `sec-passed`), авто‑комментарий, история коммитов.
4) Actions — история прогонов PR Checks и Release Pipeline с логами.
5) Insights → Network — история веток/PR/мержей.
6) DockerHub — теги по версиям и `latest`, история pull/push; описание обновляется из README.
7) Тест: делаю коммит → пушу → PR Checks → Merge → релиз.
8) Telegram — приходит сообщение о выпуске новой версии.

Docker
```
docker build -t local/pythonproject1:dev .
docker run -p 8000:8000 local/pythonproject1:dev
```
# pr среда, 15 октября 2025 г. 15:22:08 (MSK)
# pr среда, 15 октября 2025 г. 15:22:29 (MSK)
# final среда, 15 октября 2025 г. 15:37:29 (MSK)

