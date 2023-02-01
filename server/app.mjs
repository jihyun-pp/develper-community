import { express } from express;
import { morgan } from morgan;
import { cookieParser } from cookie-parser;
import { session } from express-session;
import { path } from path;
import { dotenv } from dotenv;
import { nunjucks } from nunjucks;

dotenv.config(); 
const app = express();
app.set('port', process.env.PORT || 3000);

app.use(morgan('dev')); 
