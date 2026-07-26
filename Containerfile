FROM chimeralinux/chimera AS runner

RUN apk add --no-cache \
	git python ruff flatpak shadow
RUN useradd builder

USER builder
COPY --chown=builder . /build/
WORKDIR /build
