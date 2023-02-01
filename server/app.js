const express = require('express');
const morgan = require('morgan');
const cookieParser = require('cookie-parser');
const session = require('express-session');
const path = require('path');
const dotenv = require('dotenv');
const nunjucks = require('nunjucks');

dotenv.config();  // process.env 관리를 위한 패키지

const app = express();
app.set('port', process.env.PORT || 3000);

