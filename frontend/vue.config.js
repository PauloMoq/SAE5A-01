module.exports = {
  publicPath: process.env.NODE_ENV === 'production' ? '/' : '/',
  devServer: {
    disableHostCheck: process.env.NODE_ENV === 'development',
  },
};
