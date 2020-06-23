const axios = require('axios');
const url = 'https://www.reneecbyer.com/galleries/';
const cheerio = require('cheerio');

async function scrape() {
    const html = await axios.get(url);
    const $ = await cheerio.load(html.data);
    let data = [];
  
    $('.slide').each((i, elem) => {
      if (i <= 79) {
        data.push({
          image: $(elem).find('img').attr('data-src'),
          id: $(elem).attr('data-slide-url'),
          title: $(elem).find('.slide-meta p.title').text(),
          desc: $(elem).find('.description p').first().text()
        })
      }
    });
  
    console.log(data);
}

scrape();