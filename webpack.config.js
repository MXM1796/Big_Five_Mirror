const path = require('path');
const webpack = require('webpack'); //to access built-in plugins
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    context: __dirname,
  entry: './src/index',
    mode: 'development',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: "[name]-[hash].js"
  },
    plugins: [
        new BundleTracker({path: __dirname, filename: 'webpack-stats.json'})
  ],
  resolve: {
    extensions: ['.js'],
    modules: ['node_modules'],
    fallback: {
        fs: false,
        child_process: false,
        util: require.resolve("util/"),
        "stream": require.resolve("stream-browserify"),
        "buffer": require.resolve("buffer/"),
        "path": require.resolve("path-browserify"),
         "os": require.resolve("os-browserify/browser")
      }
  }
};