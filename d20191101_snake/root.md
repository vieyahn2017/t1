/

app.json
```json
{
  "name": "react-redux-universal-hot-example",
  "description": "Example of an isomorphic (universal) webapp using react redux and hot reloading",
  "repository": "https://github.com/erikras/react-redux-universal-hot-example",
  "logo": "http://node-js-sample.herokuapp.com/node.svg",
  "keywords": [
    "react",
    "isomorphic",
    "universal",
    "webpack",
    "express",
    "hot reloading",
    "react-hot-reloader",
    "redux",
    "starter",
    "boilerplate",
    "babel"
  ]
}

```


circle.yml
```yml
machine:
  node:
    version: 4.0
  environment:
    CONTINUOUS_INTEGRATION: true

dependencies:
  cache_directories:
    - node_modules
  override:
    - npm prune && npm install

test:
  override:
    - npm run lint
    - npm test
    - npm run test-node

```



karma.conf.js
```js
var webpack = require('webpack');

module.exports = function (config) {
  config.set({

    browsers: ['PhantomJS'],

    singleRun: !!process.env.CI,

    frameworks: [ 'mocha' ],

    files: [
      './node_modules/phantomjs-polyfill/bind-polyfill.js',
      'tests.webpack.js'
    ],

    preprocessors: {
      'tests.webpack.js': [ 'webpack', 'sourcemap' ]
    },

    reporters: [ 'mocha' ],

    plugins: [
      require("karma-webpack"),
      require("karma-mocha"),
      require("karma-mocha-reporter"),
      require("karma-phantomjs-launcher"),
      require("karma-sourcemap-loader")
    ],

    webpack: {
      devtool: 'inline-source-map',
      module: {
        loaders: [
          { test: /\.(jpe?g|png|gif|svg)$/, loader: 'url', query: {limit: 10240} },
          { test: /\.js$/, exclude: /node_modules/, loaders: ['babel']},
          { test: /\.json$/, loader: 'json-loader' },
          { test: /\.less$/, loader: 'style!css!less' },
          { test: /\.scss$/, loader: 'style!css?modules&importLoaders=2&sourceMap&localIdentName=[local]___[hash:base64:5]!autoprefixer?browsers=last 2 version!sass?outputStyle=expanded&sourceMap' }
        ]
      },
      resolve: {
        modulesDirectories: [
          'src',
          'node_modules'
        ],
        extensions: ['', '.json', '.js']
      },
      plugins: [
        new webpack.IgnorePlugin(/\.json$/),
        new webpack.NoErrorsPlugin(),
        new webpack.DefinePlugin({
          __CLIENT__: true,
          __SERVER__: false,
          __DEVELOPMENT__: true,
          __DEVTOOLS__: false  // <-------- DISABLE redux-devtools HERE
        })
      ]
    },

    webpackServer: {
      noInfo: true
    }

  });
};

```


CONTRIBUTING.md

package.json
```json
{
  "name": "dog-running",
  "description": "a working dog",
  "author": "jzc",
  "license": "xxoo",
  "version": "0.0.1",
  "repository": {
    "type": "git",
    "url": "***/dog.git"
  },
  "homepage": "***/dog",
  "keywords": [
    "react",
    "isomorphic",
    "universal",
    "webpack",
    "express",
    "hot reloading",
    "react-hot-reloader",
    "redux",
    "starter",
    "babel"
  ],
  "main": "bin/server.js",
  "scripts": {
    "start": "concurrently --kill-others \"npm run start-prod\" \"npm run start-prod-api\" \"npm run start-mongod\"",
    "start-prod": "better-npm-run start-prod",
    "start-prod-api": "better-npm-run start-prod-api",
    "build": "better-npm-run build",
    "postinstall": "npm run build",
    "lint": "eslint -c .eslintrc src api",
    "start-dev": "better-npm-run start-dev",
    "start-dev-api": "better-npm-run start-dev-api",
    "watch-client": "better-npm-run watch-client",
    "dev": "concurrently --kill-others \"npm run watch-client\" \"npm run start-dev\" \"npm run start-dev-api\"",
    "dev-no-mongo": "concurrently --kill-others \"npm run watch-client\" \"npm run start-dev\" \"npm run start-dev-api\"",
    "start-mongod": "better-npm-run start-mongod",
    "test": "karma start",
    "test-node": "./node_modules/mocha/bin/mocha $(find api -name '*-test.js') --compilers js:babel-core/register",
    "test-node-watch": "./node_modules/mocha/bin/mocha $(find api -name '*-test.js') --compilers js:babel-core/register --watch",
    "pm2": "better-npm-run start-pm2"
  },
  "betterScripts": {
    "start-prod": {
      "command": "node ./bin/server.js",
      "env": {
        "NODE_PATH": "./src",
        "NODE_ENV": "production",
        "PORT": 8080,
        "APIPORT": 3030
      }
    },
    "start-prod-api": {
      "command": "node ./bin/api.js",
      "env": {
        "NODE_PATH": "./api",
        "NODE_ENV": "production",
        "APIPORT": 3030
      }
    },
    "start-dev": {
      "command": "node ./bin/server.js",
      "env": {
        "NODE_PATH": "./src",
        "NODE_ENV": "development",
        "PORT": 3000,
        "APIPORT": 3030
      }
    },
    "start-dev-api": {
      "command": "node ./bin/api.js",
      "env": {
        "NODE_PATH": "./api",
        "NODE_ENV": "development",
        "APIPORT": 3030
      }
    },
    "watch-client": {
      "command": "node webpack/webpack-dev-server.js",
      "env": {
        "UV_THREADPOOL_SIZE": 100,
        "NODE_PATH": "./src",
        "PORT": 3000,
        "APIPORT": 3030
      }
    },
    "build": {
      "command": "webpack --verbose --colors --display-error-details --config webpack/prod.config.js",
      "env": {
        "NODE_ENV": "production"
      }
    },
    "start-mongod": {
      "command": "mongod"
    },
    "start-pm2": {
      "command": "pm2 start ./process.json",
      "env": {
        "NODE_ENV": ""
      }
    }
  },
  "dependencies": {
    "antd": "^2.13.4",
    "babel-core": "^6.5.2",
    "babel-loader": "^7.1.2",
    "babel-plugin-add-module-exports": "^0.2.1",
    "babel-plugin-import": "^1.6.0",
    "babel-plugin-transform-decorators-legacy": "^1.3.4",
    "babel-plugin-transform-react-display-name": "^6.3.13",
    "babel-plugin-transform-runtime": "^6.3.13",
    "babel-polyfill": "^6.3.14",
    "babel-preset-es2015": "^6.3.13",
    "babel-preset-react": "^6.3.13",
    "babel-preset-stage-0": "^6.3.13",
    "babel-register": "^6.3.13",
    "babel-runtime": "^6.3.19",
    "bcrypt-nodejs": "0.0.3",
    "body-parser": "^1.18.2",
    "bytebuffer": "^5.0.1",
    "compression": "^1.7.1",
    "connect-mongo": "^2.0.0",
    "cookie-parser": "^1.4.3",
    "express": "^4.16.1",
    "express-session": "^1.15.6",
    "file-loader": "^1.1.5",
    "hoist-non-react-statics": "^2.3.1",
    "http-proxy": "^1.12.0",
    "immutable": "^3.8.2",
    "invariant": "^2.2.0",
    "jquery-file-upload-middleware": "^0.1.8",
    "js-cookie": "^2.1.4",
    "jsonwebtoken": "^8.1.0",
    "less": "^2.5.3",
    "less-loader": "^4.0.5",
    "log4js": "^2.3.4",
    "lru-memoize": "^1.0.0",
    "map-props": "^1.0.0",
    "mongoose": "^4.12.1",
    "multireducer": "^3.1.0",
    "piping": "^0.3.0",
    "postcss-loader": "^2.0.6",
    "pretty-error": "^2.1.1",
    "prop-types": "^15.6.0",
    "react": "^15.6.2",
    "react-dom": "^15.6.2",
    "react-helmet": "^5.2.0",
    "react-inline-css": "^2.0.0",
    "react-redux": "^5.0.6",
    "react-redux-loading-bar": "^2.9.3",
    "react-router": "^3.2.0",
    "react-router-redux": "^4.0.0",
    "redux": "^3.0.4",
    "redux-async-connect": "^1.0.0-rc4",
    "redux-thunk": "^2.1.0",
    "serialize-javascript": "^1.1.2",
    "serve-favicon": "^2.4.5",
    "socket.io": "^2.0.3",
    "socket.io-client": "^2.0.3",
    "socketio-jwt": "^4.5.0",
    "store2": "^2.5.7",
    "superagent": "^3.6.3",
    "three": "^0.87.1",
    "url-loader": "^0.6.2",
    "violet-paginator": "^2.0.6",
    "warning": "^3.0.0",
    "webpack-isomorphic-tools": "^3.0.5"
  },
  "devDependencies": {
    "autoprefixer-loader": "^3.1.0",
    "babel-eslint": "^5.0.4",
    "babel-plugin-react-transform": "^3.0.0",
    "babel-plugin-typecheck": "^3.6.0",
    "better-npm-run": "^0.1.0",
    "chai": "^3.3.0",
    "clean-webpack-plugin": "^0.1.17",
    "concurrently": "^3.5.0",
    "css-loader": "^0.28.7",
    "eslint": "1.10.3",
    "eslint-config-airbnb": "0.1.0",
    "eslint-loader": "^1.0.0",
    "eslint-plugin-import": "^0.8.1",
    "eslint-plugin-react": "^3.16.1",
    "extract-text-webpack-plugin": "^3.0.1",
    "font-awesome": "^4.4.0",
    "font-awesome-webpack": "0.0.4",
    "json-loader": "^0.5.4",
    "karma": "^0.13.10",
    "karma-cli": "^0.1.1",
    "karma-mocha": "^0.2.0",
    "karma-mocha-reporter": "^1.1.1",
    "karma-phantomjs-launcher": "^0.2.1",
    "karma-sourcemap-loader": "^0.3.5",
    "karma-webpack": "^1.7.0",
    "mocha": "^2.3.3",
    "node-sass": "^4.5.3",
    "phantomjs": "^1.9.18",
    "phantomjs-polyfill": "0.0.2",
    "react-a11y": "^0.3.4",
    "react-addons-test-utils": "0.14.8",
    "react-transform-catch-errors": "^1.0.0",
    "react-transform-hmr": "^1.0.1",
    "redbox-react": "^1.1.1",
    "redux-devtools": "^3.0.0-beta-3",
    "redux-devtools-dock-monitor": "^1.0.0-beta-3",
    "redux-devtools-log-monitor": "^1.0.0-beta-3",
    "sass-loader": "^6.0.6",
    "sinon": "^1.17.2",
    "strip-loader": "^0.1.0",
    "style-loader": "^0.19.0",
    "timekeeper": "0.0.5",
    "webpack": "^3.6.0",
    "webpack-dev-middleware": "^1.4.0",
    "webpack-hot-middleware": "^2.5.0"
  },
  "engines": {
    "node": "5.6.0"
  }
}

```



postcss.config.js
```js
module.exports = {
    plugins: [
        require('autoprefixer')
    ]
};

```



process.json
```json
{
  "apps": [
    {
      "name": "mongod",
      "script": "echo mongod --config ./mongo.conf",
      "watch": false,
      "log_date_format": "YYYY-MM-DD HH:mm Z"
    },
    {
      "name": "server",
      "script": "bin/server.js",
      "watch": true,
      "log_date_format": "YYYY-MM-DD HH:mm Z",
      "env": {
        "NODE_PATH": "./src",
        "NODE_ENV": "production",
        "PORT": 8080,
        "APIPORT": 3030
      }
    },
    {
      "name": "api",
      "script": "bin/api.js",
      "watch": true,
      "log_date_format": "YYYY-MM-DD HH:mm Z",
      "env": {
        "NODE_PATH": "./api",
        "NODE_ENV": "production",
        "APIPORT": 3030
      }
    }
  ]
}
```


README.md 

tests.webpack.js
```js
var context = require.context('./src', true, /-test\.js$/);
context.keys().forEach(context);

```
         
webpack-assets.json
```json

```



缺少

.bablerc
.eslintrc

以及
server.babel.js
```js
//  enable runtime transpilation to use ES6/7 in node

var fs = require('fs');

var babelrc = fs.readFileSync('./.babelrc');
var config;

try {
  config = JSON.parse(babelrc);
} catch (err) {
  console.error('==>     ERROR: Error parsing your .babelrc.');
  console.error(err);
}

require('babel-register')(config);
```