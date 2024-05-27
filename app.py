import streamlit as st
import os
import openai
import backoff

openai.api_key="your api key"
openai.api_base="your base_url"

st.set_page_config(
    page_title="匠心问答",
    page_icon="./image/labor.png",
    layout="centered",
    initial_sidebar_state="auto",
)

# set_page_config配置Streamlit应用程序的页面设置。自定义应用程序的标题、图标、布局等方面，以提供更好的用户体验。
# 注意：set_page_config必须在应用程序的所有其他元素之前调用，否则会引发异常。
# 参数说明：
# page_title：可选参数，用于设置应用程序的标题，通常显示在浏览器的标签页上。
# page_icon：可选参数，用于设置应用程序的图标，通常显示在浏览器标签页和书签栏中。
# layout：可选参数，用于设置应用程序的布局方式，可以是"centered"（居中）或"wide"（宽屏）。
# initial_sidebar_state：可选参数，用于设置侧边栏的初始状态。可以是"auto"（自动展开）或"collapsed"（折叠）

import streamlit as st

def init_sidebar():
    """
    初始化侧边栏
    :return:
    """

    # 自定义CSS样式
    st.sidebar.markdown(
        """
        <style>
        .sidebar-title {
            font-size: 30px;
            font-weight: bold;
            color: #333333;
            text-align: center;
            margin-top: 20px;
        }
        .sidebar-image {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
        }
        .sidebar-section {
            border: 2px solid #f0f0f0;
            padding: 10px;
            border-radius: 30px;
            margin-bottom: 30px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # 添加图标和标题
    st.sidebar.markdown('<div class="sidebar-title">劳模风范</div>', unsafe_allow_html=True)

    # 分隔符和描述
    st.sidebar.markdown('<div class="sidebar-section">展示本组ppt关键内容</div>', unsafe_allow_html=True)

    # 添加图片展示
    st.sidebar.image("./image/laomo1.png", use_column_width=True)
    st.sidebar.image("./image/laomo2.png", use_column_width=True)
    st.sidebar.image("./image/laomo3.png", use_column_width=True)
    st.sidebar.image("./image/gongjiang1.png", use_column_width=True)
    st.sidebar.image("./image/gongjiang2.png", use_column_width=True)
    st.sidebar.image("./image/gongjiang3.png", use_column_width=True)

    # 添加关于我们标题
    st.sidebar.markdown('<div class="sidebar-title">关于我们</div>', unsafe_allow_html=True)

    # 添加组员信息
    st.sidebar.subheader("团队成员")
    team_markdown = """
    - **汇报人**: 高洺策
    - **组长**: 周小渲
    - **成员**: 王瑞琪、杨畔、雷友素、王钦、刘亭秀、金萌琪
    """
    st.sidebar.markdown(team_markdown)

    # 添加联系信息或社交媒体链接
    st.sidebar.subheader("联系我们")
    st.sidebar.markdown("""
        如果你有任何问题或建议，请通过以下方式联系我们：
        - 邮箱: echoaugust2@gmail.com
        - 电话: 151-5201-2670
        - [GitHub](https://github.com/August6676)
    """)

# 调用初始化侧边栏函数
init_sidebar()


# def init_sidebar():
#     """
#     初始化侧边栏
#     :return:
#     """
#     # 设置侧边栏标题
#     st.sidebar.title("关于我们")
#
#     # 添加组员信息
#     st.sidebar.subheader("团队成员")
#     team_markdown = """
#     - **汇报人**: 高洺策
#     - **组长**: 周小渲
#     - **成员**: 王瑞琪、杨畔、雷友素、王钦、刘亭秀、金萌琪
#     """
#     st.sidebar.markdown(team_markdown)
#
#     # 添加分隔符
#     st.sidebar.markdown("---")
#
#     # 添加图标和标题
#     st.sidebar.image("./image/laomo.png", width=100)
#     st.sidebar.title("劳模风范")
#
#     # 添加描述
#     st.sidebar.info("展示劳动模范和工匠精神的相关图片和内容")
#
#     # 添加图片和描述
#     image_list = [
#         ("./image/laomo1.png", "劳动模范1"),
#         ("./image/laomo2.png", "劳动模范2"),
#         ("./image/laomo3.png", "劳动模范3"),
#         ("./image/gongjiang1.png", "工匠精神1"),
#         ("./image/gongjiang2.png", "工匠精神2"),
#         ("./image/gongjiang3.png", "工匠精神3"),
#     ]
#
#     for image_path, caption in image_list:
#         st.sidebar.image(image_path, use_column_width=True, caption=caption)
#
#     # 添加分隔符
#     st.sidebar.markdown("---")
#
#     # 添加联系信息或社交媒体链接
#     st.sidebar.subheader("联系我们")
#     st.sidebar.markdown("""
#     如果你有任何问题或建议，请通过以下方式联系我们：
#     - 邮箱: example@example.com
#     - 电话: 123-456-7890
#     - [GitHub](https://github.com/example)
#     """)
#
#
# # 调用初始化侧边栏函数
# init_sidebar()

def init_content():
    """
    初始化内容
    :return:
    """
    # Customize page title
    # st.title('<img src="D:\大二\大二下\毛概\劳模Agent\image\labor.png" alt="icon" style="vertical-align: middle;"> 劳模智能体（Agent）', unsafe_allow_html=True)
    st.title('劳模智能体 :blue[_Agent_] :sunglasses:')

    st.markdown('''
        :red[劳模] :orange[Agent，] :green[可以讲述] :blue[相关劳模] :violet[的事迹]
        :gray[以及与] :rainbow[人类进行沟通，]  :blue-background[可以作为劳模学习和教学的辅助工具] 。''')
    # 插入图片,让图片自适应

    st.image("./image/title.png",use_column_width=True)

    # st.header("Instructions")
    #
    # markdown = """
    # 1. For the [GitHub repository](https://github.com/giswqs/geemap-apps) or [use it as a template](https://github.com/new?template_name=geemap-apps&template_owner=giswqs) for your own project.
    # 2. Customize the sidebar by changing the sidebar text and logo in each Python files.
    # 3. Find your favorite emoji from https://emojipedia.org.
    # 4. Add a new app to the `pages/` directory with an emoji in the file name, e.g., `1_🚀_Chart.py`.
    # """
    #
    # st.markdown(markdown)

    # 我要构建一个交互式的应用程序，让用户可以在应用程序中输入一些内容，然后应用程序会根据用户的输入做出相应的响应。
    # 输入框，让用户输入内容
    st.header("输入✍🏻")
    text_area = st.text_area("", "在这里输入你的需求~~~~~~~~比如 你是谁？", height=100, max_chars=200)

    # 如果文本内容等于“你是谁？”，则输出“我是劳模智能体，我可以讲述相关劳模的事迹以及与人类进行沟通，可以作为劳模学习和教学的辅助工具。”
    # 写一个标题

    st.header("输出🗒️")
    # 定义一个输出框，默认输出“在这里输出模型回复~~~~~~~~”
    text = st.empty()
    # 修改输出框为多行文本框
    # output_area = st.text_area("", "在这里输出模型回复~~~~~~~~")
    # text.text("在这里输出模型回复~~~~~~~~")
    if text_area == "你是谁？":
        # st.success("我是劳模智能体，我可以讲述相关劳模的事迹以及与人类进行沟通，可以作为劳模学习和教学的辅助工具。")
        # 在输出框output_area中显示文本内容"我是劳模智能体，我可以讲述相关劳模的事迹以及与人类进行沟通，可以作为劳模学习和教学的辅助工具。你可以随意向我提出问题，我会尽力回答你的问题。"
        st.write("我是劳模智能体，我可以讲述相关劳模的事迹以及与人类进行沟通，可以作为劳模学习和教学的辅助工具。你可以随意向我提出问题，我会尽力回答你的问题。")

    else:
        @backoff.on_exception(
            backoff.fibo,
                # https://platform.openai.com/docs/guides/error-codes/python-library-error-types
            (
                openai.error.APIError,
                openai.error.Timeout,
                openai.error.RateLimitError,
                openai.error.ServiceUnavailableError,
                openai.error.APIConnectionError,
                KeyError,
            ),
        )
        def call_lm(model, messages, max_tokens, temperature, stop_words):
            try:
                response = openai.ChatCompletion.create(
                    model=model,
                    messages=messages,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    stop=stop_words
                )
                return response.choices[0].message["content"].strip()
            except Exception as e:
                st.error(f"Error: {e}")
                raise
        model = "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "你是一个劳模智能体，了解中国的劳模事迹。下面你需要回答用户提出的问题"},
            {"role": "user", "content": text_area},
        ]
        print("messages",messages)
        max_tokens = 512
        temperature = 0.9
        stop_words = []
        response = call_lm(model,messages,max_tokens,temperature,stop_words)
        print("response",response)
        st.write(response)




if __name__ == '__main__':
    init_sidebar()
    init_content()
    pass
