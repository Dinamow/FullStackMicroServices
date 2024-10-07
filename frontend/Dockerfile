# Stage 1: Install Dependencies
FROM node:18-alpine AS dependencies

RUN apk add --no-cache libc6-compat
WORKDIR /app
COPY package*.json ./
RUN npm ci


# Stage 2: Build Application
FROM node:18-alpine AS builder

WORKDIR /app
COPY --from=dependencies /app/node_modules ./node_modules
COPY . .
ENV NEXT_TELEMETRY_DISABLED 1
# Set build-time argument for Node environment
ARG NODE_ENV=production
# Set environment variable from build arg
ENV NODE_ENV=${NODE_ENV}
RUN npm run build

# Stage 3: Production Runner
FROM node:18-alpine AS runner
WORKDIR /app
# Disable Next.js telemetry in production
ENV NEXT_TELEMETRY_DISABLED 1
# Create a system group and user for security
RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

# Copy only the necessary built files from builder stage
# --chown sets the proper file ownership
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static
COPY --from=builder --chown=nextjs:nodejs /app/public ./public

# Switch to non-root user for security
USER nextjs
EXPOSE 3000
ENV PORT 3000
CMD ["node", "server.js"]