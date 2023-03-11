FROM node:lts-alpine

WORKDIR /app
RUN npm i -g puppeteer
RUN npm i puppeteer

FROM python:3.11-alpine

# Set up a directory for your Django app
WORKDIR /app

COPY --from=0 /app/node_modules/puppeteer /app/node_modules/puppeteer
# Copy your requirements.txt file and install Python dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy your Django project into the container
COPY . .

EXPOSE 8000

CMD python3 manage.py runserver 0.0.0.0:8000