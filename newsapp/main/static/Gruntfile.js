module.exports = function (grunt) {

    // 1. All configuration goes here 
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        concat: {
            js: {
                src: [
                    'bower_components/jquery/dist/jquery.min.js',
                    'bower_components/bootstrap/dist/js/bootstrap.min.js',
                ],
                dest: 'js/application.js',
            },
            css: {
                src: [
                    'bower_components/bootstrap/dist/css/bootstrap.min.css',
                    'styles/styles.css'
                ],
                dest: 'styles/application.css',
            }
        },
        
        uglify: {
            build: {
                src: 'js/application.js',
                dest: 'js/application.min.js'
            }
        },
        cssmin: {
            dev: {
                files: [{
                    expand: true,
                    cwd: 'styles/',
                    src: ['*.css', '!*.min.css'], // 1
                    dest: 'styles/',
                    ext: '.min.css'
                }]
            }
        }
        
    });

    // 3. Where we tell Grunt we plan to use this plug-in.
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-cssmin');

    // 4. Where we tell Grunt what to do when we type "grunt" into the terminal.
    grunt.registerTask('devJS', ['concat:js', 'uglify:build']);
    grunt.registerTask('devCSS', ['concat:css', 'cssmin:dev']);
};