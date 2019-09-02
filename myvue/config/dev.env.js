'use strict'
const merge = require('webpack-merge')
const prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
    // if (!isProduction) {
    //   code = prettier.format(code, { semi: false, parser: 'babylon' })
    //   code = prettier.format(code, { semi: false, parser: 'babel' })
    // }
})
