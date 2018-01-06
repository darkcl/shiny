var webpack = require('webpack');  
module.exports = {  
  entry: [
    "./js/index.js"
  ],
  output: {
    path: __dirname + '/web/static/js',
    filename: "bundle.js"
  },
  module: {
    loaders: [
      { test: /\.js$/, exclude: /node_modules/, loader: 'babel-loader?presets[]=es2015&presets[]=react' }
    ]
  },
  plugins: [
  ]
};