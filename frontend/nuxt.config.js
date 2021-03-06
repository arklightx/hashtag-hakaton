export default {
    // Target: https://go.nuxtjs.dev/config-target
    target: 'static',

    // Global page headers: https://go.nuxtjs.dev/config-head
    head: {
        title: 'SParfum',
        htmlAttrs: {
            lang: 'en'
        },
        meta: [
            { charset: 'utf-8' },
            { name: 'viewport', content: 'width=device-width, initial-scale=1' },
            { hid: 'description', name: 'description', content: '' },
            { name: 'format-detection', content: 'telephone=no' }
        ],
        link: [
            { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
            { rel: 'stylesheets', href: 'https://fonts.googleapis.com/icon?family=Material+Icons' }
        ]
    },

    // Global CSS: https://go.nuxtjs.dev/config-css
    css: [
        "assets/styles/normalize.scss",
        "assets/styles/main.scss",

    ],

    // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
    plugins: [],

    // Auto import components: https://go.nuxtjs.dev/config-components
    components: true,

    // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
    buildModules: [
        // Simple usage
        '@nuxtjs/google-fonts',

        // With options
        ['@nuxtjs/google-fonts', {
            families: {
                Roboto: { wght: [100, 400] },
            }
        }]
    ],

    // Modules: https://go.nuxtjs.dev/config-modules
    modules: [
        // Simple usage
        'cookie-universal-nuxt',

        // With options
        ['cookie-universal-nuxt', { alias: 'cookiz' }],
    ],

    // Build Configuration: https://go.nuxtjs.dev/config-build
    build: {}
}