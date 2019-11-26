/* eslint-disable camelcase */
/* eslint-disable no-plusplus */
/* eslint-disable max-classes-per-file */
/* eslint-disable no-console */
/* eslint-disable eqeqeq */
const progress = require('request-progress');
const request = require('request');
const moment = require('moment');
const fs = require('fs');

class Tradeday {
  constructor() {
    const aaa = fs.readFileSync('tradeday.json');
    this.days = JSON.parse(aaa);
  }

  findDay(date) {
    const s = date.format('YYYY-MM-DD');
    const ret = this.days.find((a) => a == s);
    return ret != undefined;
  }
}
const tradingDays = new Tradeday();
// var url = "http://www.tdx.com.cn/products/data/data/2ktic/20180131.zip";
function downloadRequest(url, end) {
  const filepath = url.split('/').reverse()[0];
  const filenamehtml = `${filepath}.html`;
  const tmpfile = `_${filepath}`;
  let result;
  let contentType;
  if (fs.existsSync(filepath)) {
    end(filepath, undefined, url);
    return;
  }

  if (fs.existsSync(filenamehtml)) {
    end(filenamehtml, undefined, url);
    return;
  }
  progress(request(url))
    .on('progress', (state) => {
      const { percent, speed } = state;
      result = state;
      console.log(url, `${(percent * 100).toFixed(2)}%`, `${(speed / 1000).toFixed(2)}K`);
    })
    .on('response', (a) => {
      contentType = a.headers['content-type'];
      console.log(contentType, url);
    })
    .on('error', (err) => {
      console.log(err);
      end(result, err, url);
    })
    .on('end', () => {
      let filename = filepath;
      if (contentType) {
        if (contentType != 'application/zip') {
          filename = filenamehtml;
        }
      }
      fs.renameSync(tmpfile, filename);
      end(filename, undefined, url);
    })
    .pipe(fs.createWriteStream(tmpfile));
}

function download_date(date, cb) {
  const days = date.format('YYYYMMDD');
  const url = `http://www.tdx.com.cn/products/data/data/2ktic/${days}.zip`;
  downloadRequest(url, cb);
}
class Download {
  constructor() {
    this.year = 2018;
    this.month = 0;
    this.day = 1;
    const { year, month, day } = this;
    this.day = moment([year, month, day]);
    this.count = 0;
    this.startloop = false;
  }

  run() {
    if (this.startloop == false) {
      this.startloop = true;
      setInterval(() => {
        this.run();
      }, 1000);
    }
    if (this.count > 10) {
      return;
    }
    const next = this.getNext();
    this.count++;
    download_date(next, (a, error, url) => {
      this.count--;
      console.log(a, error, url);
    });
  }

  getNext() {
    const { day } = this;
    let next = day.add(1, 'days');
    while (tradingDays.findDay(next) == false) {
      next = day.add(1, 'days');
    }
    this.day = next;
    return next;
  }
}
new Download().run();
