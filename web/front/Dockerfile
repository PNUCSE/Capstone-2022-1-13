FROM node:lts

WORKDIR /app
COPY .yarn ./.yarn
COPY package.json yarn.lock .yarnrc.yml craco.config.js jsconfig.json ./

RUN yarn set version berry
RUN yarn install

EXPOSE 8010
COPY . .

CMD ["yarn", "start"]