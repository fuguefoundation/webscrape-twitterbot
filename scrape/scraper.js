const axios = require('axios');
const url = 'https://example.com/';
const cheerio = require('cheerio');

async function scrape() {
    const html = await axios.get(url);
    const $ = await cheerio.load(html.data);
    let data = [];
  
    $('.my-container-element').each((i, elem) => {
      if (i <= 79) {
        data.push({
          title: $(elem).find('h4').text(),
          desc: $(elem).find('p').text(),
          url: $(elem).find('p a').attr('href')
        })
      }
    });
  
    console.log(data);
}

scrape();