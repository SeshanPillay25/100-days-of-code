const fs = require('fs')
const readTitles = function(dataURL){ 
    let titles = []
    fs.readdirSync(dataURL).forEach((file, i) => {
        if(file.split('.md').length==2){
            titles.push({
                title: `${file.split('.md')[0]}`, 
                dir: `${dataURL}/${file}` 
            })
        }
    })
   return titles
}

module.exports = {
    readTitles
};





