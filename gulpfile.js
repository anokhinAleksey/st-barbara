
"use strict";

import { task, src, dest, parallel, series, watch } from 'gulp';
import del from 'del';
import uglify from 'gulp-uglify';
import cleanCSS from 'gulp-clean-css';
import rename from "gulp-rename";
import merge from 'merge-stream';

const sass = require('gulp-sass')(require('sass'));
const autoprefixer = import('gulp-autoprefixer');
const browserSync = require('browser-sync').create();

// Clean task
task('clean', function() {
  return del(['dist', 'assets/css/app.css']);
});

// Copy third party libraries from node_modules into /vendor
task('vendor:js', function() {
  return src([
    './node_modules/bootstrap/dist/js/*',
    './node_modules/@popperjs/core/dist/umd/popper.*'
  ])
    .pipe(dest('./assets/js/vendor'));
});

// Copy bootstrap-icons from node_modules into /fonts
task('vendor:fonts', function() {
  return  src([
    './node_modules/bootstrap-icons/**/*',
    '!./node_modules/bootstrap-icons/package.json',
    '!./node_modules/bootstrap-icons/README.md',
  ])
    .pipe(dest('./assets/fonts/bootstrap-icons'))
});

// vendor task
task('vendor', parallel('vendor:fonts', 'vendor:js'));

// Copy vendor's js to /dist
task('vendor:build', function() {
  var jsStream = src([
    './assets/js/vendor/bootstrap.bundle.min.js',
    './assets/js/vendor/popper.min.js'
  ])
    .pipe(dest('./dist/assets/js/vendor'));
  var fontStream = src(['./assets/fonts/bootstrap-icons/**/*.*']).pipe(dest('./dist/assets/fonts/bootstrap-icons'));
  return merge (jsStream, fontStream);
})

// Copy Bootstrap SCSS(SASS) from node_modules to /assets/scss/bootstrap
task('bootstrap:scss', function() {
  return src(['./node_modules/bootstrap/scss/**/*'])
    .pipe(dest('./assets/scss/bootstrap'));
});

// Compile SCSS(SASS) files
task('scss', series('bootstrap:scss', function compileScss() {
  return src(['./assets/scss/*.scss'])
    .pipe(sass.sync({
      outputStyle: 'expanded'
    }).on('error', sass.logError))
    .pipe(autoprefixer.autoprefixer())
    .pipe(dest('./assets/css'))
}));

// Minify CSS
task('css:minify', series('scss', function cssMinify() {
  return src("./assets/css/*.css")
    .pipe(cleanCSS())
    .pipe(rename({
      suffix: '.min'
    }))
    .pipe(dest('./dist/assets/css'))
    .pipe(browserSync.stream());
}));

// Minify Js
task('js:minify', function () {
  return src([
    './assets/js/app.js'
  ])
    .pipe(uglify())
    .pipe(rename({
      suffix: '.min'
    }))
    .pipe(dest('./dist/assets/js'))
    .pipe(browserSync.stream());
});

// Configure the browserSync task and watch file path for change
task('dev', function browserDev(done) {
  browserSync.init({
    server: {
      baseDir: "./"
    }
  });
  watch(['assets/scss/*.scss','assets/scss/**/*.scss','!assets/scss/bootstrap/**'], series('css:minify', function cssBrowserReload (done) {
    browserSync.reload();
    done(); //Async callback for completion.
  }));
  watch('assets/js/app.js', series('js:minify', function jsBrowserReload (done) {
    browserSync.reload();
    done();
  }));
  done();
});

// Build task
task("build", series(parallel('css:minify', 'js:minify', 'vendor'), 'vendor:build', function copyAssets() {
  return src([
    "assets/img/**"
  ], { base: './'})
    .pipe(dest('dist'));
}));

// Default task
task("default", series("clean", 'build'));
