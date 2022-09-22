const CracoAlias = require('craco-alias');

module.exports = {
    devServer: {
        port: 8010
    },
    plugins: [
        {
            plugin: CracoAlias,
            options: {
                source: 'jsconfig',
                jsConfigPath: 'jsconfig.paths.json'
            }
        }
    ]
};