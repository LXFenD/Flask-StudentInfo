var gulp = require('gulp');
var cssnano = require('gulp-cssnano');
var rename = require('gulp-rename');
var uglify = require('gulp-uglify');
var bs = require('browser-sync');
var sourcemaps = require('gulp-sourcemaps');
var util = require('gulp-util');
var sass = require('gulp-sass')

gulp.task('scss', function () {
    gulp.src('./src/css/**/*.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(cssnano())
        .pipe(rename({'suffix': '.min'}))
        .pipe(gulp.dest('./dist/css/'))
        .pipe(bs.stream())
})

gulp.task('js', function () {
    gulp.src('./src/js/*.js')
        .pipe(sourcemaps.init())
        .pipe(uglify().on('error', util.log))
        .pipe(rename({'suffix': '.min'}))
        .pipe(sourcemaps.write())
        .pipe(gulp.dest('./dist/js/'))
        .pipe(bs.stream())
});

gulp.task('watch', function () {
    gulp.watch('./src/css/**/*.scss', ['scss']),
        gulp.watch('./src/js/*.js', ['js'])
});

gulp.task('bs', function () {
    bs.init({
        'server': {
            'baseDir': './'
        }
    })
});

gulp.task('default', ['bs', 'watch']);