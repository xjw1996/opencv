#include <iostream>
#include <opencv2/opencv.hpp>
// #define M_PI 3.14159265358979323846264338327950288 /* pi             */

namespace FindStopLine
{
class Core
{
    cv::Scalar range_low = cv::Scalar(0, 210, 0);
    cv::Scalar range_up = cv::Scalar(180, 255, 255);
    bool show;
    std::string show_name;
    float range_x_min = 0;
    float range_x_max = 1;
    float range_y_min = 0.4;
    float range_y_max = 1;
    float range_length = 0.6;
    int img_width;
    int img_height;

public:
    Core() : show(false)
    {
    }
    Core(std::string &set_show_name) : show(true), show_name(set_show_name)
    {
        if (show)
            cv::namedWindow(show_name, cv::WINDOW_AUTOSIZE);
    }
    // ros图片转换成cv图片
    cv::Mat ros2img()
    {
        cv::Mat img_o;
        return img_o;
    }

    cv::Mat img2bw(cv::Mat img_o)
    {
        img_width = img_o.cols;
        img_height = img_o.rows;
        cv::Mat img_bw;
        cv::cvtColor(img_o, img_bw, cv::COLOR_BGR2HSV);
        cv::inRange(img_bw, range_low, range_up, img_bw);
        return img_bw;
    }

    cv::Vec4i findMainLine(cv::Mat img_bw, cv::Mat img_o)
    {
        std::vector<cv::Vec4i> lines;
        cv::HoughLines(img_bw, lines, 1, M_PI / 360, 130, 30, 50);
        if (lines.empty())
            throw 2;
        cv::Vec4i &line_max = lines[0];
        for (cv::Vec4i li : lines)
        {
            cv::Point p1(li[0], li[1]), p2(li[2], li[3]);
            if (show)
                cv::line(img_o, p1, p2, cv::Scalar(0, 100, 0), 1);

            double line_slope = abs((p2.y - p1.y) / (p2.x - p1.x));
            int line_length = (pow(p2.x - p1.x, 2) + pow(p2.y - p1.y, 2), 0.5);
            int long_length = 0;
            if ((line_length > long_length) && (line_slope < 0.5))
            {
                line_max = li;
            }
        }
        if (show)
            cv::line(img_o, cv::Point(line_max[0], line_max[1]), cv::Point(line_max[2], line_max[3]), cv::Scalar(255, 0, 0), 3);

        return line_max;
    }

    bool checkStopLine(cv::Vec4i li)
    {
        cv::Point p1(li[0], li[1]), p2(li[2], li[3]);
        int line_length = (pow(p2.x - p1.x, 2) + pow(p2.y - p1.y, 2), 0.5);
        if (line_length < img_width * range_length)
            return false;
        int center_x = (p1.x + p2.x) / 2;
        int center_y = (p1.y + p2.y) / 2;
        if (center_x < img_width * range_x_min || center_x > img_width * range_x_max)
            return false;
        if (center_y < img_width * range_y_min || center_y > img_width * range_y_max)
            return false;
        return true;
    }

    void display(cv::Mat img)
    {
        if (show)
            cv::imshow(show_name, img);
    }
};
} // namespace FindStopLine

int main()
{
    FindStopLine::Core findstopline;

    // cv::Mat img_o(findstopline.ros2img());
    cv::Mat img_o = cv::imread("./p.jpg");
    cv::Mat img_bw = findstopline.img2bw(img_o);
    cv::Vec4i main_line = findstopline.findMainLine(img_bw, img_o);
    findstopline.display(img_o);
}
