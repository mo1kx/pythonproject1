PythonProject1 — учебный проект для демонстрации полного CI/CD пайплайна

Содержимое:
- минимальный веб‑сервис на FastAPI с `GET /health`
- тесты на pytest
- версионирование через `version.txt` и автогенерация `CHANGELOG.md`
- Dockerfile и docker-compose для запуска
- GitHub Actions: проверки PR, релиз с публикацией образа в DockerHub, обновление описания, уведомление в Telegram, деплой на self‑hosted раннер, GitHub Release

Требуемые секреты репозитория:
- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`
- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`

Как подготовить окружение и проверку:
1) Создайте репозиторий в DockerHub с именем `pythonproject1` и получите токен (Account Settings → Security → New Access Token). Заполните секреты `DOCKERHUB_USERNAME` и `DOCKERHUB_TOKEN` в GitHub → Settings → Secrets → Actions.
2) Создайте Telegram-бота через @BotFather, получите токен и добавьте его в `TELEGRAM_BOT_TOKEN`. Узнайте `chat id` вашего канала/чата (например, через добавление бота и запрос `getUpdates`) и сохраните в `TELEGRAM_CHAT_ID`.
3) Настройте self-hosted runner на локальном ПК: GitHub → Settings → Actions → Runners → New self-hosted runner → Linux/Mac/Windows. Выполните выданные команды. Дайте раннеру доступ к Docker (добавьте пользователя в группу docker или запускайте сервис от пользователя с правами docker). На хосте должен быть установлен Docker и Docker Compose V2.
4) Дайте пользователю `makarmarkov` роль Admin в репозитории (Settings → Collaborators & teams), чтобы он мог просматривать PR, Actions, сети коммитов и запускать проверки.
5) В DockerHub в разделе репозитория появится описание и README — оно обновляется автоматически в релизе.

Как работать с ветками:
- Для новых возможностей используйте ветки вида `feature/...`. Для срочных исправлений — `hotfix/...` или указывайте слово `hotfix` в сообщении коммита при мерже в `main` — от этого зависит тип увеличения версии (minor для feature, patch для hotfix).
- На Pull Request автоматически запускаются тесты и проверки безопасности. При успехе добавляются лейблы `test-passed` и `sec-passed`.
- При пуше в `main` запускается релиз: автоповышение версии (`version.txt`), обновление `CHANGELOG.md`, сборка/публикация образа в DockerHub, обновление описания репо в DockerHub, уведомление в Telegram, деплой на self-hosted, создание GitHub Release с тэгом `v<version>`.

Локальный запуск:
```
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Docker:
```
docker build -t local/pythonproject1:dev .
docker run -p 8000:8000 local/pythonproject1:dev
```

Docker Compose (используется на self-hosted деплое):
```
docker compose up -d
```

Добавление проверяющего:
- дайте доступ пользователю `makarmarkov` с ролью Admin в репозитории


