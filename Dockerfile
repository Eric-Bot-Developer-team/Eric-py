FROM gorialis/discord.py:3.9-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "command_handler.py"]