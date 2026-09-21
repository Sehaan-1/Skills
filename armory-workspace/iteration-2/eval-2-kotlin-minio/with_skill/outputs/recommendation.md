# SDK Recommendation: photo uploads to S3-compatible storage (MinIO) — Kotlin/Android

**Top pick: `aws.sdk.kotlin:s3` (Apache-2.0, v1.6.92)** — the AWS SDK for Kotlin officially targets Android, is Apache-2.0 licensed (safe for your closed-source app), and points at your MinIO cluster with a one-line endpoint override.

## Why it wins

- **License gate 5/5** — Apache-2.0 (license badge verified in the aws-sdk-kotlin repo): permissive, includes an explicit patent grant, obligations limited to keeping notices. Fully compatible with a closed-source commercial app. All three serious candidates pass the gate — so license doesn't differentiate here, it just had to be checked.
- **Android support** — the SDK's stated targets are JVM, **Android**, and GraalVM (verified from the repo README). The AWS SDK for Java v2 is not aimed at Android — that's exactly the gap the Kotlin SDK exists to fill.
- **Maintenance 5/5** — v1.6.92 published ~2026-06-09 (live Maven Central data, 700+ published versions, AWS-backed).
- **DX 4/5** — official developer guide, AWS code-examples repo, idiomatic Kotlin DSL (`PutObjectRequest { ... }`), coroutine-based suspend APIs.

## Comparison

| Candidate | Performance | Maintenance | License | DX | Weighted |
|---|---|---|---|---|---|
| `aws.sdk.kotlin:s3` | 4/5 | 5/5 | ✅ Apache-2.0 | 4/5 | **4.5/5** |
| `io.minio:minio` (Java client) | 3/5 | 4/5 | ✅ Apache-2.0 | 3/5 | **3.8/5** |
| `software.amazon.awssdk:s3` (Java v2) | 3/5 | 5/5 | ✅ Apache-2.0 | 2/5 | **3.8/5** |

Weights used: 25/25/25/25 (no priorities stated). Data provenance: Maven Central's *search* index reported the MinIO client at 8.5.17, but the canonical `maven-metadata.xml` shows **9.0.3, released 2026-06-12** — the canonical record was used. Licenses: Apache-2.0 for the AWS SDKs confirmed from repo/docs; the MinIO client's Apache-2.0 is from knowledge — a 30-second LICENSE-file check before shipping is recommended. Considered and dropped: raw OkHttp + SigV4 hand-signing — possible, but re-implementing S3 auth yourself is exactly what an SDK saves you from.

## Trade-offs

- **Dependency footprint**: the Kotlin SDK pulls the smithy-kotlin runtime + an HTTP engine into your APK. Check the size impact against your app budget; R8 helps. The MinIO Java client is leaner but not officially Android-validated — expect occasional JVM-assumption surprises on device.
- **Java v2 SDK** is the best-documented S3 client on the JVM, but it's built for servers; running it on Android is unsupported territory. It's the right answer for your *backend*, not your app.
- ⚠️ **Architecture note**: hard-coding storage credentials into a mobile app is a security anti-pattern — anyone can extract them. The usual production pattern is your backend minting **presigned PUT URLs** (server-side) while the app does a plain HTTPS PUT. Worth deciding before you commit to in-app credentials.

## Getting started

```kotlin
// build.gradle.kts
implementation("aws.sdk.kotlin:s3:1.6.92")
```

```kotlin
import aws.sdk.kotlin.services.s3.S3Client
import aws.sdk.kotlin.services.s3.model.PutObjectRequest
import aws.sdk.kotlin.runtime.auth.credentials.StaticCredentialsProvider
import aws.smithy.kotlin.runtime.content.asByteStream
import java.io.File

val s3 = S3Client {
    region = "us-east-1"                                 // MinIO accepts any region
    endpointUrl = "https://minio.yourcompany.com"        // point at your cluster
    forcePathStyle = true                                // required for MinIO / S3-compatible endpoints
    credentialsProvider = StaticCredentialsProvider {
        accessKeyId = "YOUR_MINIO_ACCESS_KEY"
        secretAccessKey = "YOUR_MINIO_SECRET_KEY"
    }
}

suspend fun uploadPhoto(userId: String, file: File) {
    val request = PutObjectRequest {
        bucket = "photos"
        key = "$userId/${file.name}"
        body = file.asByteStream()
        contentType = "image/jpeg"
    }
    s3.putObject(request)
}
```

## Assumptions & caveats

- Assumed a Gradle/Android pipeline and a modern `minSdk`; verify the SDK's current `minSdk` floor against yours in the developer guide.
- The exact `endpointUrl` assignment syntax varies slightly between SDK versions (string vs `Url.parse(...)`); the pinned-version API reference is the source of truth — check before copying blindly. `forcePathStyle = true` is the non-negotiable part for MinIO.
- Project license assumed closed-source per your message; Apache-2.0 keeps you clean either way.
