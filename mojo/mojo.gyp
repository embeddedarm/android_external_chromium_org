# Copyright 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
    'chromium_code': 1,
  },
  'target_defaults': {
    'defines': ['MOJO_IMPLEMENTATION'],
  },
  'targets': [
    {
      'target_name': 'mojo',
      'type': 'none',
      'dependencies': [
        'mojo_public_test_support',
        'mojo_public_unittests',
        'mojo_public_perftests',
        'mojo_system',
        'mojo_system_unittests',
      ],
    },
    {
      'target_name': 'mojo_public_test_support',
      'type': 'static_library',
      'dependencies': [
        '../base/base.gyp:base',
        '../testing/gtest.gyp:gtest',
        'mojo_system',
      ],
      'sources': [
        'public/tests/test_support.cc',
        'public/tests/test_support.h',
      ],
    },
    {
      'target_name': 'mojo_public_unittests',
      'type': 'executable',
      'dependencies': [
        '../base/base.gyp:run_all_unittests',
        '../testing/gtest.gyp:gtest',
        'mojo_public_test_support',
        'mojo_system',
      ],
      'sources': [
        'public/tests/system_core_unittest.cc',
      ],
    },
    {
      'target_name': 'mojo_public_perftests',
      'type': 'executable',
      'dependencies': [
        '../base/base.gyp:base',
        '../base/base.gyp:test_support_perf',
        '../testing/gtest.gyp:gtest',
        'mojo_public_test_support',
        'mojo_system',
      ],
      'sources': [
        'public/tests/system_core_perftest.cc',
      ],
    },
    {
      'target_name': 'mojo_system',
      # TODO(vtl): This should probably be '<(component)'; make it work.
      'type': '<(component)',
      'dependencies': [
        '../base/base.gyp:base',
      ],
      'defines': [
        'MOJO_SYSTEM_IMPLEMENTATION',
      ],
      'sources': [
        'system/core.cc',
        'system/core_impl.cc',
        'system/core_impl.h',
        'system/dispatcher.cc',
        'system/dispatcher.h',
        'system/limits.h',
        'system/local_message_pipe_endpoint.cc',
        'system/local_message_pipe_endpoint.h',
        'system/memory.cc',
        'system/memory.h',
        'system/message_in_transit.cc',
        'system/message_in_transit.h',
        'system/message_pipe.cc',
        'system/message_pipe.h',
        'system/message_pipe_dispatcher.cc',
        'system/message_pipe_dispatcher.h',
        'system/message_pipe_endpoint.cc',
        'system/message_pipe_endpoint.h',
        'system/platform_channel_handle.h',
        'system/raw_channel.h',
        'system/raw_channel_posix.cc',
        'system/simple_dispatcher.cc',
        'system/simple_dispatcher.h',
        'system/waiter.cc',
        'system/waiter.h',
        'system/waiter_list.cc',
        'system/waiter_list.h',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '..',
        ],
      },
    },
    {
      'target_name': 'mojo_system_unittests',
      'type': 'executable',
      'dependencies': [
        '../base/base.gyp:run_all_unittests',
        '../testing/gtest.gyp:gtest',
        'mojo_system',
      ],
      'sources': [
        'system/core_impl_unittest.cc',
        'system/core_test_base.cc',
        'system/core_test_base.h',
        'system/dispatcher_unittest.cc',
        'system/message_pipe_dispatcher_unittest.cc',
        'system/message_pipe_unittest.cc',
        'system/raw_channel_posix_unittest.cc',
        'system/simple_dispatcher_unittest.cc',
        'system/test_utils.h',
        'system/waiter_list_unittest.cc',
        'system/waiter_test_utils.cc',
        'system/waiter_test_utils.h',
        'system/waiter_unittest.cc',
      ],
    },
    {
      'target_name': 'mojo_shell',
      'type': 'executable',
      'dependencies': [
        '../base/base.gyp:base',
        'mojo_system',
      ],
      'sources': [
        'shell/app_container.cc',
        'shell/app_container.h',
        'shell/shell.cc',
        'shell/switches.cc',
        'shell/switches.h',
      ],
      'conditions': [
        ['OS == "win"', {
          # TODO(jschuh): crbug.com/167187 fix size_t to int truncations.
          'msvs_disabled_warnings': [
            4267,
          ],
        }],
      ],
    },
    {
      'target_name': 'sample_app',
      'type': '<(component)',
      'dependencies': [
        '../base/base.gyp:base',
        'mojo_system',
      ],
      'sources': [
        'shell/sample_app.cc',
      ],
    },
    {
      'target_name': 'mojo_bindings',
      'type': 'static_library',
      'include_dirs': [
        '..'
      ],
      'sources': [
        'public/bindings/lib/bindings.h',
        'public/bindings/lib/bindings_internal.h',
        'public/bindings/lib/bindings_serialization.cc',
        'public/bindings/lib/bindings_serialization.h',
        'public/bindings/lib/buffer.cc',
        'public/bindings/lib/buffer.h',
        'public/bindings/lib/message.cc',
        'public/bindings/lib/message.h',
        'public/bindings/lib/message_builder.cc',
        'public/bindings/lib/message_builder.h',
      ],
    },
    {
      'target_name': 'mojo_bindings_test',
      'type': 'executable',
      'include_dirs': [
        '..'
      ],
      'dependencies': [
        'mojo_bindings',
      ],
      'sources': [
        'public/bindings/sample/generated/sample_service.h',
        'public/bindings/sample/generated/sample_service_proxy.cc',
        'public/bindings/sample/generated/sample_service_serialization.h',
        'public/bindings/sample/generated/sample_service_stub.cc',
        'public/bindings/sample/sample_test.cc',
      ],
    },
  ],
}