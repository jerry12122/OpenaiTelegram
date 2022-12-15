FROM python
RUN pip install openai && \
pip install python-telegram-bot
WORKDIR /app
COPY . .
ENTRYPOINT ["python","main.py"]