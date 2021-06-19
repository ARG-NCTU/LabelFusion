FROM argnctu/locobot:NUC-sis

USER root

############################# lcm #################################
RUN cd ${HOME} && git clone https://github.com/lcm-proj/lcm \
    && cd lcm \
    && mkdir build \
    && cd build \
    && cmake .. \
    && make install

