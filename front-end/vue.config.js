module.exports = {
  publicPath: './',
  outputDir: '../server/templates',
  assetsDir: process.env.NODE_ENV === 'production' ? '../static' : '',
}
