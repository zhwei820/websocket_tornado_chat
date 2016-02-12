var webpack = require('webpack')
var path = require('path')
var ExtractTextPlugin = require('extract-text-webpack-plugin');
var vue = require('vue-loader');


module.exports = {
  entry: './chatroom/index.js',
  output: {
    path: './static',
    publicPath: '/static/',
    filename: 'build.js'
  },
  resolve: {
    root: path.resolve('./')
  },
  module: {
    loaders: [
      {test: /\.vue$/, loader: 'vue' },
      {
      	test: /\.js$/,
        exclude: /node_modules|vue\/src|vue-router\/|vue-loader\/|vue-hot-reload-api\//,
      	loader: 'babel'
      },
      { test: /\.css$/, loader: "style-loader!css-loader?root=./mall/" }
      ,
      {
      test: /\.(png|jpg)$/,
      loader: 'url-loader?limit=100000&name=mall/assets/img/[hash:8].[name].[ext]'
    },

    ]
  },
  vue: {
    loaders: {
      less: ExtractTextPlugin.extract('css!less')
    }
  },
  plugins: [
     new ExtractTextPlugin('./app.css'), // 输出到 output path 下的 app.css 文件
   ],
  babel: {
  presets: ['es2015'],
  plugins: ['transform-runtime']
},
  devtool: 'source-map'
};


if (process.env.NODE_ENV === 'production') {
  delete module.exports.devtool;
  module.exports.plugins = [
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: '"production"'
      }
    }),
    new webpack.optimize.UglifyJsPlugin({
      compress: {
        warnings: false
      }
    })
  ];
}
